import React, { useState } from 'react';

const table = () => {
  const [rows, setRows] = useState([
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
  ]);

  const input = (e, rowIndex, colIndex) => {
    const newRows = [...rows];
    newRows[rowIndex][colIndex] = e.target.value;
    setRows(newRows);
  };

  return (
    <div>
      <table>
        <tbody>
          {rows.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, colIndex) => (
                <td key={colIndex}>
                  <input
                    type="text"
                    value={cell}
                    onChange={(e) => input(e, rowIndex, colIndex)}
                  />
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default table;