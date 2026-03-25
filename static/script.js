let selectedMood = "";

$(".mood-card").click(function () {

    // Remove highlight from all
    $(".mood-card").removeClass("selected");

    // Add highlight to clicked one
    $(this).addClass("selected");

    // Store selected mood
    selectedMood = $(this).data("mood");
    $("#selectedMood").val(selectedMood);

    // Show language section (if you added it)
    $("#languageSection").removeClass("d-none").hide().fadeIn(400);
});

$("#moodForm").submit(function (e) {
    if (selectedMood === "") {
        alert("Please select a mood!");
        e.preventDefault();
    }
});