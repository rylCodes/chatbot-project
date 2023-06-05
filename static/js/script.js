function getUserResponse() {
    var userText = $('#textInput').val().trim();
    if (userText === '') {
        return; // Exit the function if the input is empty or contains only whitespace
    }
    var userHTML = `<div class="mb-4 flex flex-col">
                        <div class="border-2 max-w-2xl bg-white text-gray-800 py-2 px-4 rounded-lg self-end">${userText}</div>
                        <p class="text-xs text-gray-500 self-end mt-1">You</p>
                    </div>`;
    $('#textInput').val("");
    $('#chatbot').append(userHTML);
    $('#chatbot').scrollTop($('#chatbot')[0].scrollHeight);
    $('#textInput').focus();

    $.get('/getResponse/', {userMessage: userText}).done(function(data) {
        var chatbotHTML = `<div class="mb-4 flex flex-col">
                                <div class="max-w-2xl bg-gray-800 py-2 px-4 rounded-lg self-start text-white border-2 border-black">${data}</div>
                                <p class="text-xs text-gray-500 self-start mt-1">chatterBC</p>
                            </div>`;
        $('#chatbot').append(chatbotHTML);
        $('#chatbot').scrollTop($('#chatbot')[0].scrollHeight);
    });
}

$('#buttonInput').click(function() {
    getUserResponse();
});

$('#textInput').keydown(function(event) {
    if (event.key === 'Enter') {
        getUserResponse();
        event.preventDefault();
    }
});
