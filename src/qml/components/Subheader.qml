import QtQuick 2.7

Rectangle {
    property color dividerColor: "#EEE"
    property alias text: label.text

    anchors.left: parent.left
    anchors.right: parent.right

    color: "#FAFAFA"
    height: 28

    Label {
        id: label
        anchors.fill: parent

        font.weight: Font.Medium
        leftPadding: 10
        verticalAlignment: Text.AlignVCenter
    }

    Rectangle {
        anchors {
            left: parent.left
            right: parent.right
            top: parent.top
        }

        height: 1
        color: dividerColor
    }

    Rectangle {
        anchors {
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }

        height: 1
        color: dividerColor
    }
}
