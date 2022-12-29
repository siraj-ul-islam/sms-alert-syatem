let projectId= 0;
let campaignId= 0;
$(document).ready(function(){
    $("#selectProject").click(function(){
         projectId = $(this).val();
         $("#campaignSelect").empty();

        /* append campaign record */

        $("#campType").html('-')
        $("#totalSessionNumber").html('-')
        $("#totalSessionNumber").html('-')
        $("#sessionNumber").html('-')
        $("#sessionNumber").html('-')
        $("#successNumber").html('-')



        /* close */


         getProject();
    })
    $("#campaignSelect").click(function(){
         campaignId = $(this).val();
          /* append camapaign record */
            $("#campType").html('-')
            $("#totalSessionNumber").html('-')
            $("#totalSessionNumber").html('-')
            $("#sessionNumber").html('-')
            $("#sessionNumber").html('-')
            $("#successNumber").html('-')

          /* close */

         getResultRecords();
    })

})


function getProject(){
    $.ajax({
       url: '/dashboard/get-campaign/',
       data:{
            'project-id':projectId,
       },
      type:"GET",
      success: function(response, xhr){
            const data = JSON.parse(response);

            size = data.length


            $("#campaignSelect").empty();
            $("#campaignSelect").prepend(`<option>Select campaign</option>`)

            for(var i=0;i<size;i++){
                $("#campaignSelect").append('<option value='+ data[i]['pk'] +'>' +data[i]['fields']['campaign_name']+ '</option>');
            }
      },
      error:function(response, xhr){
            $("#campaignSelect").prepend(`<option>Select campaign</option>`)
      }
    })
 }

 /* get result record  */
 function  getResultRecords(){
    $.ajax({
       url: '/dashboard/get-result-records/',
       data:{
            'campaign-id':campaignId,
       },
      type:"GET",
      success: function(response, xhr){
            let data  =  JSON.parse(response['data2']);
            campaign_data=response['campaign_data']

            const campaign_type  =  response['campaign_type'];

            let daily_scheduled = campaign_data.daily_scheduled
            let campaign_success = campaign_data.campaign_sucess
            let daily_session_completed = campaign_data.daily_session_completed
            size = data.length
          /* append camapaign record */

            $("#campType").html(campaign_type)
            $("#totalSessionNumber").html(campaign_type)
            $("#totalSessionNumber").html(daily_scheduled)
            $("#sessionNumber").html(daily_session_completed)
            $("#sessionNumber").html(daily_session_completed)
            $("#successNumber").html(campaign_success)
          /* close */


            serverSideDataTable(campaignId);
      },
      error:function(response, xhr){
             $("#searchResult").append(`<tr>There is no record against this campaign</tr>`)

      }
    })
 }


function serverSideDataTable(){
 $(document).ready(function () {
    data_url="/dashboard/result-record/"+campaignId+"/"
    let listingRecords = $('#datatablesearch').DataTable({
        'serverSide': false,
        'pageLength':10,
        'ordering': false,
        'searching': true,
        'destroy':true,
        'select': false,
        'processing': false,
        "info":false,
        'deferRender': true,
        "dom": '<"top"f>rt<"bottom"ilp><"clear">',
        'ajax': {
                url: data_url,
                data: 'data',
            },
        columns:  [
                { "data":  function getNameAndEmail(data, type, dataToSet)
                        {
                        return (`<td>
                                    `+data.fields.search_date_time+`
                                </td>`);
                        }
                },
                {
                "data": function getNameAndEmail(data, type, dataToSet) {
                        return (`<td>
                                    `+data.fields.search_success+`
                                </td>`);
                    }
                },
                { "data": function getNameAndEmail(data, type, dataToSet) {
                        return (`<td>
                                    `+data.fields.session_duration+`
                                </td>`);
                    }
                },

        ],
    autoWidth: false,
    columnDefs: [
        {
            targets: ['_all'],
            className: 'mdc-data-table__cell'
        }
    ],

    });

});


}