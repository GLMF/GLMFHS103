function descriptor()
    return {
        title = "Hello VLC addons !";
	version = "1.0";
	author = "Tristan Colombo <tristan@gnulinuxmag.com>";
	url = "";
	shortdesc = "Hello world addon";
	description = "<div style=\"background-color:lightgreen;\"><b>Open a dialog box</b></div>";
}
end

function activate()
   vlc.msg.dbg("=> Function activate()");
   create_dialog();
end

function deactivate()
    vlc.msg.dbg("=> Bye !");
    if dlg then
        dlg:delete();
    end
end

function close()
    vlc.deactivate();
end

function create_dialog()
    vlc.msg.dbg("=> Function create_dialog()");
    dlg = vlc.dialog("Hello VLC addons !");
    w1 = dlg:add_label("<b>Hello !</b>", 1, 1, 1, 1);
    w2 = dlg:add_button("OK", function () return click_exit(dlg) end, 2, 1, 1, 1);
end

function click_exit(dlg)
    vlc.msg.dbg("=> Function click_exit()");
    if dlg then
        dlg:delete();
    end
end
