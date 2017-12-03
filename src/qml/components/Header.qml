import QtQuick 2.7
import ".."

Rectangle {
    anchors.left: parent.left
    anchors.right: parent.right

    height: 75
    color: "#F8F5E5"

    Column {
        anchors.centerIn: parent

        Label {
            anchors.horizontalCenter: parent.horizontalCenter
            font.pointSize: 18
            font.weight: Font.Medium

            text: Qt.formatTime(DateTime.now)
        }

        Label {
            anchors.horizontalCenter: parent.horizontalCenter
            font.weight: Font.Medium
            color: Theme.secondaryTextColor

            text: Qt.formatDate(DateTime.now, 'dddd, MMM d')
        }
    }

    Rectangle {
        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }

        height: 1
        color: "#979797"
        opacity: 0.4
    }
}
