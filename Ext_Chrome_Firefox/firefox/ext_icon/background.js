ACTIVE_DOMAIN = 'connect.ed-diamond.com';

chrome.browserAction.onClicked.addListener(function(tab) {
    let domain = new URL(tab.url);
    if (domain.hostname != ACTIVE_DOMAIN) {
        console.log('The domain ' + domain.hostname + ' is not active.\nTry with ' + ACTIVE_DOMAIN);
        return;
    };

    function getReference() {
        function copyToClipboard(str) {
            var clipboard = document.createElement('textarea');
            clipboard.value = str;
            clipboard.setAttribute('readonly', '');
            clipboard.style = {position: 'absolute', left: '-9999px'};
            document.body.appendChild(clipboard);

            clipboard.select();
            document.execCommand('copy');
   
            document.body.removeChild(clipboard);
        }

        let reference = "";
        try {
            let title = document.getElementsByClassName("breadcrumb")[0].children[3].children[0].innerHTML;
            let author = document.getElementsByClassName("auteurs")[0].children[0].innerHTML;
            let magazine = document.getElementsByClassName("breadcrumb")[0].children[1].children[0].innerHTML;
            let number = document.getElementsByClassName("numero")[0].children[0].innerHTML;
            let date = document.getElementsByClassName("date")[0].innerHTML;
            reference = author +', "' + title + '", ' + magazine + ' ' + number + ', ' + date + ' : ' + window.location.href;
            reference = reference.replace(/\n/g, "");
        }
        catch (error) {
            return "";
        }

        copyToClipboard(reference);
        return reference;
    }

    chrome.tabs.executeScript({
        code: "(" + getReference + ")();"
    }, (results) => {
        if (results == "") {
            console.log("No reference in page");
        } else {
            console.log("Reference copied in clipboard :\n" + results);
        }
    });
});
