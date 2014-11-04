ascendRest
==========

API calls 
// AJAX Request: Add item (https://glacial-springs-8093.herokuapp.com/tags/)

<pre><code>
$.ajax({
     url: "https://glacial-springs-8093.herokuapp.com/tags/",
     type: "POST",
     timeout: 30000,

     // HTTP Headers: https://glacial-springs-8093.herokuapp.com/tags/

     headers:{
          "Content-Type":"application/json",
     },

     // Request Body: https://glacial-springs-8093.herokuapp.com/tags/

     data:"{\"parseId\": \"objId\", \"name\": \"https\"}",

     // Success Callback: https://glacial-springs-8093.herokuapp.com/tags/

     success:function(data, textStatus) {
          console.log("Received response HTTP "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/)");
          console.log(data);
     },

     // Error Callback: https://glacial-springs-8093.herokuapp.com/tags/

     error:function(jqXHR, textStatus, errorThrown) {
          console.log("Error during request "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/)");
          console.log(errorThrown);
     },
});
</code></pre>


// AJAX Request: Search for item (https://glacial-springs-8093.herokuapp.com/tags/search/test)

$.ajax({
     url: "https://glacial-springs-8093.herokuapp.com/tags/search/test",
     type: "GET",
     timeout: 30000,

     // Success Callback: https://glacial-springs-8093.herokuapp.com/tags/search/test

     success:function(data, textStatus) {
          console.log("Received response HTTP "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/search/test)");
          console.log(data);
     },

     // Error Callback: https://glacial-springs-8093.herokuapp.com/tags/search/test

     error:function(jqXHR, textStatus, errorThrown) {
          console.log("Error during request "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/search/test)");
          console.log(errorThrown);
     },
}); 


// AJAX Request: Tag List (https://glacial-springs-8093.herokuapp.com/tags/)
<pre><code>
$.ajax({
     url: "https://glacial-springs-8093.herokuapp.com/tags/",
     type: "GET",
     timeout: 30000,

     // Success Callback: https://glacial-springs-8093.herokuapp.com/tags/

     success:function(data, textStatus) {
          console.log("Received response HTTP "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/)");
          console.log(data);
     },

     // Error Callback: https://glacial-springs-8093.herokuapp.com/tags/

     error:function(jqXHR, textStatus, errorThrown) {
          console.log("Error during request "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/)");
          console.log(errorThrown);
     },
});
</code></pre>

// AJAX Request: Delete item (https://glacial-springs-8093.herokuapp.com/tags/objID)
<code><pre>
$.ajax({
     url: "https://glacial-springs-8093.herokuapp.com/tags/objID",
     type: "DELETE",
     timeout: 30000,

     // Success Callback: https://glacial-springs-8093.herokuapp.com/tags/objID

     success:function(data, textStatus) {
          console.log("Received response HTTP "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/objID)");
          console.log(data);
     },

     // Error Callback: https://glacial-springs-8093.herokuapp.com/tags/objID

     error:function(jqXHR, textStatus, errorThrown) {
          console.log("Error during request "+textStatus+" (https://glacial-springs-8093.herokuapp.com/tags/objID)");
          console.log(errorThrown);
     },
});
</pre></code>

// AJAX Request: JQuery autocomplete (https://glacial-springs-8093.herokuapp.com/frontend/jquery?term=t)
<pre><code>
$.ajax({
     url: "https://glacial-springs-8093.herokuapp.com/frontend/jquery?term=t",
     type: "GET",
     timeout: 30000,

     // Success Callback: https://glacial-springs-8093.herokuapp.com/frontend/jquery?term=t

     success:function(data, textStatus) {
          console.log("Received response HTTP "+textStatus+" (https://glacial-springs-8093.herokuapp.com/frontend/jquery?term=t)");
          console.log(data);
     },

     // Error Callback: https://glacial-springs-8093.herokuapp.com/frontend/jquery?term=t

     error:function(jqXHR, textStatus, errorThrown) {
          console.log("Error during request "+textStatus+" (https://glacial-springs-8093.herokuapp.com/frontend/jquery?term=t)");
          console.log(errorThrown);
     },
});
</code></pre>
