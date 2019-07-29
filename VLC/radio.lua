STATIONS = {
    { name = "TSF Jazz", url = "http://tsfjazz.ice.infomaniak.ch/tsfjazz-high.mp3" },
    { name = "Jazz Radio", url = "http://jazzradio.ice.infomaniak.ch/jazzradio-high.mp3" },
    { name = "Jazz Radio Blues", url = "http://jazzblues.ice.infomaniak.ch/jazzblues-high.mp3" },
}

function descriptor()
    return {
        title = "Radio Selector",
	version = "1.0",
	author = "Tristan Colombo <tristan@gnulinuxmag.com>",
	url = "",
	shortdesc = "Radio Selector",
	description = "<div style=\"background-color:lightgreen;\"><b>Radio Selector</b></div>",
    }
end

function activate()
    dlg = vlc.dialog("Radio Selector")
    display_main(dlg)
end

function deactivate()
    vlc.msg.info("=> Bye !")
end

function close()
    vlc.deactivate()
end

function meta_changed()
   t = get_now_playing()
   vlc.msg.info("Now playing:")
   vlc.msg.info(t)
end

function get_now_playing(str)
    local item = vlc.item or vlc.input.item()
    if not item then
        return ""
    end
    local metas = item:metas()
    if metas["now_playing"] then
        return metas["now_playing"]
    else
        return ""
    end
end

function display_main(dlg)
    dlg:set_title("Radio Selector")
    list = dlg:add_list(1, 3, 4, 1)
    button_play = dlg:add_button("Play", function () click_play(list, button_play, dlg) end, 1, 4, 4, 1)

    for idx, details in ipairs(STATIONS) do
        list:add_value(details.name, idx)
    end
    dlg:show()
end

function click_play(list, button_play, dlg)
    local sel = nil
    local playlistItem = {}
    local selection = list:get_selection()

    for idx, selectedItem in pairs(selection) do
        sel = idx
        break
    end
    
    if sel == nil then
        vlc.msg.err("No selection !")
        display_warning(list, button_play, dlg)
    else
        vlc.msg.dbg("=> " .. STATIONS[sel].name .. " (" .. sel ..") selected with url " .. STATIONS[sel].url)
        playlistItem.path = STATIONS[sel].url
        vlc.playlist.clear()
        vlc.playlist.add({playlistItem})
        vlc.playlist.play()
    end
end

function display_warning(list, button_play, dlg)
    vlc.msg.dbg("Warning message")
    dlg:set_title("Warning !")
    dlg:del_widget(list)
    dlg:del_widget(button_play)
    w1 = dlg:add_label("You must choose an entry before clicking on 'Play' button !", 1, 1, 1, 1)
    w2 = dlg:add_button("Ok", function () return click_ok(dlg, w1, w2) end, 2, 1, 1, 1)
    dlg:update()
end

function click_ok(dlg, w1, w2)
    vlc.msg.dbg("Closing warning dialog box")
    dlg:del_widget(w1)
    dlg:del_widget(w2)
    display_main(dlg)
end
