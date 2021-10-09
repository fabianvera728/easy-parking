/* eslint-disable @typescript-eslint/naming-convention */
export interface User {
    phone_number: string;
    reputation?: number;
    picture: string;
    biography: string;
    user: {
        id?: number;
        password: string;
        last_login?: string;
        is_superuser: boolean;
        username: string;
        first_name: string;
        last_name: string;
        email: string;
        is_staff: boolean;
        is_active: boolean;
        date_joined: string;
        create_at: string;
        update_at: string;
        groups: any[];
        user_permissions: any[];
    };
}
