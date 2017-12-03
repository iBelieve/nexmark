import QtQuick 2.7
import "../components"

Column {
    anchors.left: parent.left
    anchors.right: parent.right

    property alias title: subheader.text
    property alias placeholder: placeholderLabel.text

    property alias itemHeight: listView.height
    property alias model: listView.model
    property alias delegate: listView.delegate

    Subheader {
        id: subheader
    }

    ListView {
        id: listView
        anchors.left: parent.left
        anchors.right: parent.right

        clip: true
        visible: count > 0
        orientation: Qt.Horizontal

        Scrollbar {
            flickable: listView
            orientation: listView.orientation
        }
    }

    Item {
        anchors.left: parent.left
        anchors.right: parent.right
        height: 100
        visible: listView.count == 0

        Label {
            id: placeholderLabel
            anchors.centerIn: parent
            opacity: 0.75
        }
    }
}
