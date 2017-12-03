import QtQuick 2.7
import QtQuick.Window 2.2 as Win
import "home"

Win.Window {
    id: app

    visible: true

    HomeScreen {
        id: homeScreen

        anchors.fill: parent
    }

    function newWindow(path, args) {
        if (!args) args = {}

        args.parent = app

        var component = Qt.createComponent(path)
        if (component.status === Component.Error) {
            console.error("Unable to load object: " + path + "\n" + component.errorString())
            return null
        }

        return component.createObject(app, args)
    }
}
