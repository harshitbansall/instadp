function Search() {
    $("#loaderFrame").show();
    $.ajax({
        type: "POST",
        url: "/returnImage",
        data: {
            content: $("#SearchInputBox").val(),
        },
        success: function (result) {
            $("#loaderFrame").hide();
            document.getElementById('imageFrame').innerHTML = "<img src='data:image/jpeg;base64," + result + "'>";
        }
    });
}

function EnterEventSearch() {
    if (event.key === 'Enter') {
        Search();
    }
}
