    const fetchNewExpenses = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/refresh', {
                method: 'POST',
    
            })

        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };
    


export default fetchNewExpenses;
