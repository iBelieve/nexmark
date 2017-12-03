import QtQuick 2.7
import QtQuick.Window 2.2
import "home"

Window {
    id: app

    visible: true

    HomeScreen {
        id: homeScreen

        anchors.fill: parent
    }
}
