const api = async (endpoint: string, config: {}) => {
  try {
    const response = await fetch(`http://localhost:8000/${endpoint}`, config);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error:", error);
    return error;
  }
};

export default api;
