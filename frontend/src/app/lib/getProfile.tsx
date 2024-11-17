import axios from 'axios';

export const GetProfile = async ({ id }: { id: string }) => {
  try {
    const response = await axios.get(`http://go.itatmisis.ru:8000/get_profile/${id}`);
    return response.data;
  } catch (e) {
    console.error(e);
  }
};
