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
}
