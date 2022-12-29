"use strict";
const userId = JSON.parse(document.getElementById('json-user_name').textContent);
  const  socket = new WebSocket('ws://'
  +window.location.host
  + '/ws/'
  +userId+'/')
  socket.onmessage = function(event){
       const data = JSON.parse(event.data);
       console.log("test",data)
       let divElements = document.getElementById("app")
       if (divElements.children.length !=5){
            document.querySelector("#app").style.display ="none";
           appendNotification();
      }

      function appendNotification(){
        if(data.payload == 1){
                document.querySelector("#app").style.display ="none";
                document.querySelector("#notification").innerHTML +=(`
                <a class="dropdown-item" href="#">
                    <div class="d-flex align-items-center mb-1">
                        <div class="icon icon-sm bg-indigo text-white">
                            <i class="fa fa-bell"></i>
                        </div>
                        <div class="text ms-2">
                                <p class="mb-0"> Campaign has started</p>
                        </div>
                    </div>
                </a>
                `);
           }
           else if(data.payload==0){
           document.querySelector("#app").style.display ="none";
                document.querySelector("#notification").innerHTML +=(`
                <a class="dropdown-item" href="#">
                    <div class="d-flex align-items-center mb-1">
                        <div class="icon icon-sm bg-indigo text-white">
                            <i class="fa fa-bell"></i>
                        </div>
                        <div class="text ms-2">
                                <p class="mb-0"> Campaign has closed</p>
                        </div>
                    </div>
                </a>`
                );
          }
          else{
          document.querySelector("#app").style.display ="none";
                document.querySelector("#notification").innerHTML =(`
                <a class="dropdown-item" href="#">
                    <div class="d-flex align-items-center">
                        <div class="icon icon-sm bg-indigo text-white">
                            <i class="fa fa-bell"></i>
                        </div>
                        <div class="text ms-2">
                                <p class="mb-0"> There is no notification yet</p>
                        </div>
                    </div>
                </a>
                `);
          }
      }

 }

