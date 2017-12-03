import QtQuick 2.7
import "../components"

Item {
    property var book

    width: 130

    Image {
        id: image

        anchors.centerIn: parent

        width: source.width/source.height * height
        height: parent.height - 30

        fillMode: Image.PreserveAspectFit
        source: book.cover
        mipmap: true

        layer.enabled: true
        layer.effect: Elevation {
            elevation: 2
        }
    }
}
