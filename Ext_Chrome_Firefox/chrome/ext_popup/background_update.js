chrome.runtime.onInstalled.addListener(function() {
    chrome.tabs.create({
        "url": chrome.extension.getURL('html/update.html')
    });
    console.log("Extension Updated !");

    chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
        chrome.declarativeContent.onPageChanged.addRules([{
            conditions: [new chrome.declarativeContent.PageStateMatcher({
                pageUrl: {hostEquals: 'connect.ed-diamond.com'},
            })],
            actions: [new chrome.declarativeContent.ShowPageAction()]
        }]);
    });
});
