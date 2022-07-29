import './Board.css'
import React from "react";

class Cell extends React.Component {
    render(props) {
        return (
            <td class="cell">{this.props.value}</td>
        );
    }
}

class NoCell extends React.Component {
    render() {
        return (
            <td class="nocell"></td>
        );
    }
}

export {
    Cell,
    NoCell
};