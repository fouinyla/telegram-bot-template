Telegram.WebApp.ready();

    var initDataUnsafe = Telegram.WebApp.initDataUnsafe || {};

    function sendMessage() {
        if (!initDataUnsafe.query_id) {
            alert('WebViewQueryId not defined');
            return;
        }
        $('button').prop('disabled', true);
        let text = $('textarea#message_input').val();
        $('#status').text('Sending...').removeClass('ok err').show();
        $.ajax({
            url: '/admin/sendmessage', 
            async: true,
            type: "post",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({
                text: text
            }),
            success: function(){
                $('#status').html('Message sent successfully!').addClass('ok').show();
            },
            error: function(xhr, status, error) {
                $('#status').text(status).addClass('err').show();
                alert(error)
            },
            complete: function(){
                $('button').prop('disabled', false);
            }
        });
    }

    function webviewClose() {
        Telegram.WebApp.close();
    }

    Telegram.WebApp.onEvent('themeChanged', function () {
        $('#theme_data').html(JSON.stringify(Telegram.WebApp.themeParams, null, 2));
    });

    $('body').css('visibility', '');
    Telegram.WebApp.MainButton
        .setText('CLOSE WEBVIEW')
        .show()
        .onClick(function () {
            webviewClose();
        });


    function round(val, d) {
        var k = Math.pow(10, d || 0);
        return Math.round(val * k) / k;
    }


    Telegram.WebApp.onEvent('viewportChanged', setViewportData);
    setViewportData();