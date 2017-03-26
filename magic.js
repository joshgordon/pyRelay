function update() 
{ 
		
	var strToFill = "<table><tr>"; 
	var http = createRequestObject();
	if(http) {
		http.open('get', '/api/state');
		http.onreadystatechange = function() {
			if(http.readyState == 4){
					
				//actually update the contents of the box. 
				var data = JSON.parse(http.responseText);
				for (var ii = 1; ii <= data.length; ii++) {
  				if (data[ii - 1]) {
            strToFill += "<td><img src=\"/switch-on.jpg\" height=\"128px\" onclick=\"off(" + ii + ")\"></td>"
          } else { 
            strToFill += "<td><img src=\"/switch-off.jpg\" height=\"128px\" onclick=\"on(" + ii + ")\"></td>"
          }
        }
        document.getElementById('switches').innerHTML = strToFill; 
				
      }
    };
    http.send(null);
  }
} 



//copied from the course website. Does some magic ajax stuff to get the right kind of
//ajax object based on browser type 
function createRequestObject() {
  var ro = false;
  if (window.XMLHttpRequest) {             // Mozilla, Safari, ...
    ro = new XMLHttpRequest();
  } else if (window.ActiveXObject) {       // IE < 7.0 
    try {
      ro = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
      try {
        ro = new ActiveXObject("Microsoft.XMLHTTP");
      } catch (e) { }
    }
  }
  return ro;
}


function realOff(num)
{ 
		var http = createRequestObject();
		if(http) {
				http.open('get', '/api/' + num + '/off');
				http.onreadystatechange = function() {
						if(http.readyState == 4){
								
								update(); 
						}
				};
				http.send(null);
		}
}

function off(num)
{ 
    realOff(num);
}


function on(num)
{
		var http = createRequestObject();
		if(http) {
				http.open('get', '/api/' + num + '/on');
				http.onreadystatechange = function() {
						if(http.readyState == 4){
								
								update(); 
						}
				};
				http.send(null);
		}
}
