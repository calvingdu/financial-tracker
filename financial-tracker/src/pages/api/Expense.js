    import React, { useEffect } from 'react';
    import DataMapper from './Chart';


    const Expense = ({data, setData}) => {

        useEffect(() => {
            fetchData()
                .then(data => setData(data)).catch(error => console.error("can't catch promise", error));
        }, [setData]);

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

    export const fetchData = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/get-expenses');
            const responseData = await response.json();

        return responseData;
        } catch (error) {
            console.error('Error fetching data:', error);
            throw error;
        }
    };


    export default Expense;
