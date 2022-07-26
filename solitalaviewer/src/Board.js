import React from 'react';
import './Board.css';
import {Cell, NoCell} from './Cell';
import boards from "./data/board";

class Board extends React.Component {
    state = {
        current: 0,
        boards: boards,
    }
    render() {
        const board = this.state.boards[this.state.current];
        return (
            <div>
                <div>
                    <table>
                        {board.map((row, i) => (
                            <tr>
                                {row.map((col, j) => (
                                    <td>{board[i][j]}</td>
                                ))}
                            </tr>
                        ))}
                    </table>

                </div>
                <div>
                    <button>Next</button>
                    <button>Prev</button>
                </div>
            </div>
        );
    }
}

export default Board;