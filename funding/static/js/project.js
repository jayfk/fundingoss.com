$(document).ready(function(){
   // Listener
    $(document).on("input", "#searchProjectInput", function(){
        filter();
        sort();
        console.log("fired");
    });

    $(document).on("change", "#fundingSelect", function(){
        filter();
        sort();
    });

    $(document).on("click", ".dropdown-item", function(){
       $("#orderButton").html($(this).html());
        filter();
        sort();
    });

    //
    function filter(){
        var search = $("#searchProjectInput").val().toLowerCase();
        var funding = $("#fundingSelect").val();
        $(".project").each(function () {
            $(this).show();

            // filter by name
            if(search.length >= 1){
                if($(this).data("name").toLowerCase().indexOf(search) == -1){
                    $(this).hide();
                }
            }

            // filter by funding status
            if(funding != "all" && $(this).data("funding") != funding){
                $(this).hide();
            }

        });

    }

    function sort(){
        // not yet implemented
        var order = $("#orderButton").children("span").data("order");
    }

});
