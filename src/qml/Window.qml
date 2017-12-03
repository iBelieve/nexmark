import QtQuick 2.7

Rectangle {
    id: window

    property var from
    property rect fromRect

    color: "white"
    parent: app
    width: parent.width
    height: parent.height

    state: "preview"

    states: [
        State {
            name: "preview"

            PropertyChanges {
                target: window
                x: fromRect.x
                y: fromRect.y
                width: fromRect.width
                height: fromRect.height
                color: Qt.rgba(255,255,255,0)
            }
        },
        State {
            name: "maximized"
        }
    ]

    transitions: [
        Transition {
            to: "maximized"
            PropertyAnimation {
                target: window; properties: "x,y,width,height,color"; duration: 250;
            }
        }
    ]

    MouseArea {
        anchors.fill: parent
    }

    Component.onCompleted: {
        fromRect = window.mapFromItem(from, 0, 0, from.width, from.height)
        state = "maximized"
    }
}
