# Neighborhood Map Project

## Introduction ##
This single page application shows a map of favourite destinations in Chongqing that contains map location markers and scenery list in which you can filter the specific destination by typing text.

## To do list ##
- Show a map of favourite destinations location markers and scenery list in Chongqing. 
- Click the specific item of scenery list or the marker to show the information window which contains the best photo of the place fetched from Foursquare. 
- Offer a field input box to quick select the specific place.
- Handle and tell the user the errors of loading google map and fetching data from Foursquare.
## Libraries and Frameworks ##
- [jQuery](https://jquery.com/)
- [Knockout.js](http://knockoutjs.com/)
- [Bootstrap](https://getbootstrap.com/)
## API ##
- [Google Maps API](https://cloud.google.com/maps-platform/) 
- [Foursquare API](https://developer.foursquare.com/) 
## Project Structure ##
```
├── css
│   ├── main.css
│   ├── bootstrap.min.modal.css
│   └── bootstrap.min.css
├── index.html
├── js
│   ├── app.js
│   ├── model.js
│   ├── jquery-3.3.1.min.js
│   ├── knockout-3.4.2.js
│   └── bootstrap.min.js
└── README.md
```
## Quick Start ##
- Download the source code from my repo.
- Run the app by double click`index.html`in your browser.

## Reference ##
* [ Udacity course Full-Stack Foundations Code repository](https://github.com/udacity/ud330)
* [http://www.knockmeout.net/](http://www.knockmeout.net/)
* [Foursquare for Developers](https://developer.foursquare.com/)
* [Google Maps APIs](https://developers.google.com/maps/)
* [Knockout Documentation](http://knockoutjs.com/documentation/introduction.html)

## Notice
* Because the Foursquare API Of this App was provided by the free account,it exists the API Call Quota per day .
* If you need to make more Foursquare API Calls per day ,please to log in Foursquare account and upgrade the account .
  then create this APP and update the Client ID and Client Secret in `app.js`.

