import Api from '@/endpoint/Api'

export default {
    login () {
        return Api.get('session');
    }
}