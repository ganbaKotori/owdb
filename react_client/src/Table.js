// src/Table.js
import React from 'react';
import { useGlobalFilter, useTable, useAsyncDebounce, useFilters, useSortBy, usePagination } from 'react-table';
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/react/solid";

  // Define a default UI for filtering
  function GlobalFilter({
    preGlobalFilteredRows,
    globalFilter,
    setGlobalFilter,
  }) {
    const count = preGlobalFilteredRows.length
    const [value, setValue] = React.useState(globalFilter)
    const onChange = useAsyncDebounce(value => {
      setGlobalFilter(value || undefined)
    }, 200)
  
    return (
      <span>
        Search:{' '}
        <input
          value={value || ""}
          onChange={e => {
            setValue(e.target.value);
            onChange(e.target.value);
          }}
          placeholder={`${count} records...`}
        />
      </span>
    )
  }

// src/Table.js

// This is a custom filter UI for selecting
// a unique option from a list
export function SelectColumnFilter({
  column: { filterValue, setFilter, preFilteredRows, id },
}) {
  // Calculate the options for filtering
  // using the preFilteredRows
  const options = React.useMemo(() => {
    const options = new Set();
    preFilteredRows.forEach((row) => {
      options.add(row.values[id]);
    });
    return [...options.values()];
  }, [id, preFilteredRows]);

  // Render a multi-select box
  return (
    <select
      name={id}
      id={id}
      value={filterValue}
      onChange={(e) => {
        setFilter(e.target.value || undefined);
      }}
    >
      <option value="">All</option>
      {options.map((option, i) => (
        <option key={i} value={option}>
          {option}
        </option>
      ))}
    </select>
  );
}

function Table({ columns, data }) {
	// Use the state and functions returned from useTable to build your UI
	const {
		getTableProps,
		getTableBodyProps,
		headerGroups,
		page,
		prepareRow,

    canPreviousPage,
    canNextPage,
    pageOptions,
    pageCount,
    gotoPage,
    nextPage,
    previousPage,
    setPageSize,

		state,
		preGlobalFilteredRows,
		setGlobalFilter
	} = useTable(
		{
			columns,
			data
		},
		useGlobalFilter,
    useFilters,
    useSortBy,
    usePagination, 
	);

	// Render the UI for your table
	return (
    <>
    {/* global search and filter */}
    {/* table */}
    <div className="mt-2 flex flex-col">
      <div className="-my-2 overflow-x-auto -mx-4 sm:-mx-6 lg:-mx-8">
        <div className="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
          <div className="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
            <table {...getTableProps()} className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                {headerGroups.map(headerGroup => (
                  <tr {...headerGroup.getHeaderGroupProps()}>
                    {headerGroup.headers.map(column => (
                      // Add the sorting props to control sorting. For this example
                      // we can add them into the header props
                      <th
                        scope="col"
                        className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                        {...column.getHeaderProps(column.getSortByToggleProps())}
                      >
                        {column.render('Header')}
                        {/* Add a sort direction indicator */}
                        <span>
                          {column.isSorted
                            ? column.isSortedDesc
                              ? ' ▼'
                              : ' ▲'
                            : ''}
                        </span>
                      </th>
                    ))}
                  </tr>
                ))}
              </thead>
              <tbody
                {...getTableBodyProps()}
                className="bg-white divide-y divide-gray-200"
              >
                {page.map((row, i) => {  // new
                  prepareRow(row)
                  return (
                    <tr {...row.getRowProps()}>
                      {row.cells.map(cell => {
                        return (
                          <td
                            {...cell.getCellProps()}
                            className="px-6 py-4 whitespace-nowrap"
                          >
                            {cell.render('Cell')}
                          </td>
                        )
                      })}
                    </tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    {/* Pagination */}
    <div className="pagination">
<button onClick={() => gotoPage(0)} disabled={!canPreviousPage}>
  {'<<'}
</button>{' '}
<button onClick={() => previousPage()} disabled={!canPreviousPage}>
  {'<'}
</button>{' '}
<button onClick={() => nextPage()} disabled={!canNextPage}>
  {'>'}
</button>{' '}
<button onClick={() => gotoPage(pageCount - 1)} disabled={!canNextPage}>
  {'>>'}
</button>{' '}
<span>
  Page{' '}
  <strong>
    {state.pageIndex + 1} of {pageOptions.length}
  </strong>{' '}
</span>
<select
  value={state.pageSize}
  onChange={e => {
      setPageSize(Number(e.target.value))
  }}
>
  {[5, 10, 20].map(pageSize => (
      <option key={pageSize} value={pageSize}>
      Show {pageSize}
    </option>
  ))}
</select>
</div>
<div>
{/* new */}
<pre>
  <code>{JSON.stringify(state, null, 2)}</code>
</pre>
</div>

  </>
	);
}

export default Table;
