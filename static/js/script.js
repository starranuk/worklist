 // jQuery for Materialize sidenav-trigger
 //$(document).ready(function () {
  //$(".sidenav").sidenav({edge: "right"});
//});

/*
    JavaScript for Materialize NavBar 
*/

document.addEventListener('DOMContentLoaded', function () {
     let sidenavs = document.querySelectorAll(".sidenav");
     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
 });

 /*
    jQuery for Materialize accordion element
*/
 $(document).ready(function(){
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
  });