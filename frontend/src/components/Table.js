import React from "react";

const Table = ({ headers, data }) => {
  return (
    <table className="min-w-full border-collapse border border-gray-200">
      <thead>
        <tr className="bg-gray-100">
          {headers.map((header) => (
            <th key={header} className="border border-gray-300 p-2">
              {header}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index} className="border border-gray-300">
            {headers.map((header) => (
              <td key={header} className="p-2 border border-gray-300">
                {row[header]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
