import axios from 'axios';

export const GetAllProfiles = async ({ page, limit }: { page: number; limit: number }) => {
  try {
    const response = await axios.get(
      `http://go.itatmisis.ru:8000/get_profiles/?offset=${page * limit}&limit=${limit}`,
    );
    return response.data;
  } catch (error) {
    console.error(error);
    throw error;
  }
};
