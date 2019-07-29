chrome.runtime.onInstalled.addListener(function() {
    chrome.tabs.create({
        "url": chrome.extension.getURL('html/update.html')
    });
    console.log("Extension Updated !");
});
