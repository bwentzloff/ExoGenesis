import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:8000", // Backend URL
  timeout: 10000, // 10 seconds timeout
});

// Fetch the galaxy data
export const getGalaxy = async () => {
  try {
    const response = await apiClient.get("http://127.0.0.1:8000/galaxy");
    return response.data;
  } catch (error) {
    console.error("Error fetching galaxy data:", error);
    throw error; // Re-throw to handle it in the component
  }
};
