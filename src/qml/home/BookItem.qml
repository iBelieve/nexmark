import QtQuick 2.7
import "../components"

Item {
    property var book

    width: 120
    height: 180

    Column {
        anchors {
            topMargin: 15
            bottomMargin: 10
            leftMargin: 5
            rightMargin: 5
            fill: parent
        }
        spacing: 10

        Image {
            anchors.horizontalCenter: parent.horizontalCenter
            width: source.width/source.height * height
            height: parent.height - parent.spacing - label.height

            fillMode: Image.PreserveAspectFit
            source: book.cover
        }

        Label {
            id: label

            anchors.left: parent.left
            anchors.right: parent.right
            height: implicitHeight * maximumLineCount/lineCount

            text: book.title
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.Wrap
            maximumLineCount: 2
        }
    }
}
