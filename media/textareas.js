/**
 * Created by IrshaadTechnologies on 11/15/2016.
 */

tinymce.init({
    mode: "textareas",
    theme: "advanced",
    theme_advanced_toolbar_location: "top",
    theme_advanced_toolbar_align: "left",
    plugins: "table, save, advhr, advimage, advlink, emotions, iespell, insertdatetime, preview",
    theme_advanced_buttons1: "fullscreen, seperator, preview, separator, bold, italic, underline, strikethrough, seperator, bullist, numlist, outdent, indent,seperator, undo, redo, seperator, link, unlink, anchor, separator, image, cleanup, help, separator, code",
    auto_cleanup_word: true,
    plugin_insertdate_dateFormat: "%m/%d/%Y",
    plugin_insertdate_timeFormat: "%H:%M:%S",
    extend_valid_elements: "a[name|href|target=_blank|title|onclick], img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name], hr[class|width|size|noshade], font[face|size|color|style], span[class|align|style]"
});