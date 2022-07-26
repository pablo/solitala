import React from "react";

class Cell extends React.Component {
    render() {
        return (
            <td>X</td>
        );
    }
}

class NoCell extends React.Component {
    render() {
        return (
            <td>D</td>
        );
    }
}

export {
    Cell,
    NoCell
};