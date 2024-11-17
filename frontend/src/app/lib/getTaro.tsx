import axios from 'axios';

export const GetTaro = async ({ id }: { id: string }) => {
  try {
    const response = await axios.get(`http://go.itatmisis.ru:8000/get_taro/?id=${id}&status=three`);
    return response.data;
  } catch (e) {
    console.error(e);
  }
};
