function doGet(request) {
    return HtmlService.createTemplateFromFile('CellularAutomata')
        .evaluate();
}

function include(filename) {
    return HtmlService.createHtmlOutputFromFile(filename)
        .getContent();
}
