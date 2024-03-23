import React, { useState, useEffect } from 'react';
import DataMapper from './Json';


const Expense = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/get-expenses'); // Assuming your React app is served from the same domain as FastAPI
            const responseData = await response.json();
            setData(responseData);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div>
            {data ? (
                <DataMapper jsonData={data} />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default Expense;
