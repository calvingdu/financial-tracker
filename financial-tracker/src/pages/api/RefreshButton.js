import React from 'react';
import fetchNewExpenses from './RefreshNewExpenses';
import fetchData from './Expense';

    function Button() {
        const callOtherFunctions = () => {
            fetchData();
            fetchNewExpenses();
        }
        return (
            <>
                <button 
                onClick={ callOtherFunctions }
                style={{width: "100px", height: "10px"}}
                children="Refresh"
                /> 
            </>
        )
    };

export default Button