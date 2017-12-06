import QtQuick 2.7
import QtQuick.Window 2.2

Item {
    id: cover

    property size maxSize
    property alias source: image.source
    property alias fillMode: image.fillMode

    implicitWidth: image.implicitWidth/Screen.devicePixelRatio
    implicitHeight: image.implicitHeight/Screen.devicePixelRatio

    Image {
        id: image

        anchors.fill: parent

        asynchronous: true

        sourceSize.width: maxSize.width * Screen.devicePixelRatio
        sourceSize.height: maxSize.height * Screen.devicePixelRatio

        mipmap: true
    }
}
