$("document").ready(function(){
       let dataId=0
       var projectName=""

       /* Delete Project */
       $("#delete-project").click(function(){
            console.log("test")
            dataId = $(this).attr('data');
            console.log("select data \t\t",dataId)
       });
       $("#deleteRecord").click(function(){
            let boolValue = $(this).val();
            console.log(dataId)
            if(boolValue == 'true'){
                deleteProject(dataId);
            }
       });
       function deleteProject(data_id){
            $.ajax({
               url: '/dashboard/delete-project/',
               data:{
                    'data-id':data_id,
               },
              type:"GET",
              success: function(response, xhr){
                  if(response=="true"){
                    $("#row-"+ dataId).remove();
                  }
                  else{
                       console.log("Data not deleted")
                   }
              }
            });
       }

      /* Edit Project */
      $(".edit-project").click(function(){
          dataId = $(this).attr('data');
          let projectName = $("#project-"+ dataId).text();
          $("#projectName").val(projectName);
      });

      $("#saveRecord").click(function(){
            projectName = $("#projectName").val();
            editProject(dataId,projectName)
      });
      function editProject(dataId,projectName){
        $.ajax({
           url: '/dashboard/update-project/',
           data:{
                'data-id':dataId,
                'project-name':projectName,
           },
          type:"GET",
          success: function(response, xhr){
              if(response){
                $("#project-"+ dataId).text(projectName);
              }
              else{
                   console.log("Data not updated")
              }
          }
        });
      }

    });