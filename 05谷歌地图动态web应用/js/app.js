//Google Maps Error Handling.
var mapError = function() {
    alert('Cant\'t load Google Maps!');
};
// mapDefinition object used to define the properties that can be set on a Map.
var mapDefinition = {
    center: {
        lat: 29.5666310000,
        lng: 106.5877770000
    },
    zoom: 13,
    mapTypeControl: true,
    zoomControl: true,
};
// Declare global variables about google map which can be cited by any functions below.
var map,
    infowindow,
    bounds;

// The starting point of this App which is called when the page is loaded.
function startApp() {
// Creates a new map inside of the given HTML container, which is typically a DIV element.
    map = new google.maps.Map(document.getElementById("map"), mapDefinition);
// Creates an info window with the given options.
    infowindow = new google.maps.InfoWindow({
        maxWidth: 200,
        content: "",
    });
// Add the event which means to close the infowindow after clicking the map.
    map.addListener("click", function () {
        infowindow.close(infowindow);
    });
// Constructs a rectangle from the default point including one that crosses the 180 degrees longitudinal meridian.
    bounds = new google.maps.LatLngBounds();
// Add the event which means to recenter map to contain the given bounds.
    window.addEventListener('resize',function () {
        map.fitBounds(bounds);
    });
// Apply bindings to the ViewModel.
    ko.applyBindings(new Viewmodel());
}
// Create place object.
var placeModel = function (place) {

    var self = this;
// Create place object properties and assign the value.
    this.name = place.name;
    this.location = place.location;
    this.FS_id = place.FS_id;
// Create the FS_getData property to keep track of whether can get data from Foursquare or not when state changes.
    this.FS_getData = ko.observable(true);
    this.FS_placeUrl = "";
    this.FS_bestphotoUrl = "";
// Create the visibleMarker property to keep track of whether the place marker is visible or not when state changes.
    this.visibleMarker = ko.observable(true);

    // Foursquare API Url parameter
    var FS_prefix_url = "https://api.foursquare.com/v2/venues/",
    FS_client_id = "client_id=ILO4OSRRP1ZPRLOM4W21FMD0EIQ5OLOSAFATFR3KZP1PITG5",
    FS_client_secret = "&client_secret=YJEXPOPZCH4TDJULVOHULVZP1EJXKDEWHPEAOOFQBGZQ2LBX",
    FS_version = "&v=20180323";
    // Concatenate url parameters above to generate the request url.
    var FsResquestUrl = FS_prefix_url + this.FS_id + "/?" + FS_client_id + FS_client_secret + FS_version;

    // Fetch data from Foursquare to assign properties of the place.
    $.getJSON(FsResquestUrl).done(function(data) {
        var results = data.response.venue ? data.response.venue : "";
        self.FS_placeUrl = results["shortUrl"];
        self.FS_bestphotoUrl = results.bestPhoto["prefix"] + "height150" + results.bestPhoto["suffix"];
    }).fail(function() {
        self.FS_getData(false);
    });

    // Creates a marker of the place object upon the map .
    this.marker = new google.maps.Marker({
        map: map,
        title: this.name,
        opacity: 1,
        animation: google.maps.Animation.DROP,
        position: this.location
         });
    // Create the filterMarkers property to renders the marker automatically according to the property of visibleMarker
    this.filterMarkers = ko.computed(function () {
    if(self.visibleMarker() === false) {
        // Remove the marker of the place.
        self.marker.setMap(null);
    } else {
        //Renders the marker of the place on the map
        self.marker.setMap(map);
        //Sets the viewport to contain the given bounds.
        map.fitBounds(bounds);
        //Extends this bounds to contain the position of the marker.
        bounds.extend(self.marker.position);
    }
});

// Add the click event about the marker.
    this.marker.addListener("click", function() {
        //Change the center of the map by the given distance in pixels.
        map.panBy(0, -200);
        //Change the center of the map to the location of the place
        map.panTo(this.position);
        //Open this InfoWindow on the given map.
        infowindow.open(map,this);
        //Set the infowindow content.
        infowindow.setContent(outputContent(self));
        //Start an animation of BOUNCE.
        this.setAnimation(google.maps.Animation.BOUNCE);
        //Put off 1400ms to stop BOUNCE animation.
        setTimeout(function() { self.marker.setAnimation(null);}, 1400);
        });
    // Create the itemClick property to trigger the click event of the place marker automatically
    this.itemClick = ko.observable(function() {
        google.maps.event.trigger(self.marker, 'click');
    });
}
//  Creates Formatted HTML string to display in InfoWindow according to the state of whether can get data from Foursquare or not.
function outputContent(place) {
    var normalStr =
        '<h3>' + place.name + '</h3>' +
        '<br>'+
        '<div class="infowindow">'+
            '<img src="'+ place.FS_bestphotoUrl + '" alt="Photo Loading">'+
            '<br>'+
            '<a href="' + place.FS_placeUrl +'">Know more from Foursquare.</a>' +
        '</div>';
    var failureStr =
        '<h3>' + place.name + '</h3>' +
        '<h4 >Can\'t fetch data from Foursquare.</h4>';
    if (place.FS_getData() === true) {
        return normalStr;
    }
    else {
        return failureStr;
    }
}


function Viewmodel() {

    var self = this;
// Create the sceneryList object array to keep track of place models after filtered and update UI automatically.
    this.sceneryList = ko.observableArray();
// Create the filterText String to keep track of User input string.
    this.filterText = ko.observable("");
//According to the initialList to generate object array sceneryList.
    initialList.forEach(function(item){
        self.sceneryList.push(new placeModel(item));
    });
// Create the filteredPlaces object array to renders the marker and list automatically according to the filter result.
    this.filteredPlaces = ko.computed(function () {
        var searchItem = self.filterText().toLowerCase();
        if(searchItem){
            return ko.utils.arrayFilter(self.sceneryList(),function (item) {
                var num = item.name.toLowerCase().indexOf(searchItem);
                if (num === -1) {
                    item.visibleMarker(false);
                    return false;
                }
                else {
                    item.visibleMarker(true);
                    return true;
                }
            })
        }
        else{
            self.sceneryList().forEach(function (item){
            item.visibleMarker(true);});
            return self.sceneryList();
        }
    }, self);
}







