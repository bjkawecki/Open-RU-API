export async function api (endpoint: string, config: {}) {
    try {
      const response = await fetch(`http://localhost:4000/${endpoint}`, config);
      if (!response.ok) {
        throw new Error("Network response was not ok.");
      }
      console.log(response)
      return response;
    } catch (error) {
      console.error("Error:", error);
      return error;
    }
  };
  
  