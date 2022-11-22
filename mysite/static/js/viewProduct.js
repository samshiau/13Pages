$("button").click(function (event) {
    var class_name = event.target.className.split(" ");

    if (class_name[1] == "view-product")
    {
        var _hidden_area_id = this.id + "_top_area";
        var _hidden_area = document.getElementById(_hidden_area_id);
        _hidden_area.hidden = true;
    }
    else if (class_name[1] == "back") {
        var _hidden_area_id = this.id + "_top_area";
        var _hidden_area = document.getElementById(_hidden_area_id);
        _hidden_area.hidden = false;
    }
});