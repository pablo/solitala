import React from 'react';
import './Board.css';
import {Cell, NoCell} from './Cell';
import boards from "./data/board";

class Board extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            current: 0,
            boards: boards,
        };
        this.next = this.next.bind(this);
        this.prev = this.prev.bind(this);
    };

    next = (e) => {
        e.preventDefault();
        let newCurrent = this.state.current + 1;
        if (newCurrent > 32) {
            newCurrent = 32;
        }
        console.log("new current: " + newCurrent);
        this.setState(
            {
                current: newCurrent
            }
        );
    };

    prev = (e) => {
        e.preventDefault();
        let newCurrent = this.state.current - 1;
        if (newCurrent < 0) {
            newCurrent = 0;
        }
        this.setState({
            current: newCurrent
        });
    };

    render() {
        const board = this.state.boards[this.state.current];
        return (
            <div>
                <div>
                    <table>
                        <tbody>
                        {board.map((row, i) => (
                            <tr>
                                {row.map((cell, j) => {
                                    if (cell !== '#')
                                        return <Cell key={i + "__" + j} value={cell} />;
                                    else
                                        return <NoCell key={i + "__" + j} />;
                                })
                                }
                            </tr>
                        ))}
                        </tbody>
                    </table>

                </div>
                <div>
                    BOARD: {this.state.current}
                </div>
                <div>
                    <button onClick={this.prev}>Prev</button>
                    <button onClick={this.next}>Next</button>
                </div>
            </div>
        );
    }
}

export default Board;