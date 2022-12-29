
let data_id=0;
let projectName=""

function deleteFun(dataId){
        data_id=dataId
        var project_name=document.getElementById("project-"+dataId+"")
        console.log(project_name.innerText,dataId);
        // deleteProject(dataId)
    }
function confirmDelete(){
    console.log("confirm",data_id)
    $.ajax({
       url: '/dashboard/delete-project/',
       data:{
            'data-id':data_id,
       },
      type:"GET",
      success: function(response, xhr){
            $("#row-"+ data_id).remove();
            window.location.href = window.location.href;
      }
    });
}
/* Edit Project */
function editFunction(data){
    data_id=data
    var project_name=document.getElementById("project-"+data+"")
    var project_Name = project_name.innerText
    document.getElementById("projectName").value = project_Name

    console.log(projectName)
}
function updateProject(){
projectName=document.getElementById("projectName").value
$.ajax({
           url: '/dashboard/update-project/',
           data:{
                'data-id':data_id,
                'project-name':projectName,
           },
          type:"GET",
          success: function(response, xhr){
                $("#project-"+ data_id).text(projectName);
                window.location.href = window.location.href;
          }
        });
}
/* update record */

function updateRecord(){
$(".sk-three-bounce").show()
    $.ajax({
          url: '/dashboard/get-datetime/',
          type:"GET",
          success: function(response, xhr){
                $(".sk-three-bounce").hide()
                $(".date-time time").html(response);

                window.location.href = window.location.href;

          }
        });
}

/* notification */
"use strict";

document.addEventListener("DOMContentLoaded", function () {
    // var toastElList = [].slice.call(document.querySelectorAll(".toast"));
    //
    // var toastList = toastElList.map(function (toastEl) {
    //     return new bootstrap.Toast(toastEl);
    // });

    var toastButtonList = [].slice.call(document.querySelectorAll(".toast-btn"));

    toastButtonList.map(function (toastButtonEl) {
        toastButtonEl.addEventListener("click", function () {
            var toastToTrigger = document.getElementById(toastButtonEl.dataset.target);

            if (toastToTrigger) {
                var toast = bootstrap.Toast.getInstance(toastToTrigger);
                toast.show();
            }
        });
    });
});

$("document").ready(function(){
    $('#toast').delay(5000).fadeOut('slow');
})