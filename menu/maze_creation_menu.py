import pygame_menu


class MazeCreationMenu:
    def __init__(self, window_size):
        self.__window_size = window_size
        self.__maze_creation_menu = custom_maze_creation_menu = pygame_menu.Menu(
            height=self.__window_size[1],
            width=self.__window_size[0],
            title='Create your maze',
            theme=pygame_menu.themes.THEME_DARK
        )
        self.__current_state_widgets = self.__add_choice_widgets()

    def __remove_current_state_widgets(self):
        for widget in self.__current_state_widgets:
            self.maze_creation_menu.remove_widget(widget)
        self.__current_state_widgets = []

    def __add_choice_widgets(self):
        return [
            self.maze_creation_menu.add.button('Add', lambda: self.__change_state(
                lambda: self.__add_cell_input(
                    'Add Wall',
                    lambda: self.__change_state_with_action(self.__add_wall, self.__add_choice_widgets)
                )
            )),
            self.maze_creation_menu.add.button('Remove', lambda: self.__change_state(
                lambda: self.__add_cell_input(
                    'Remove Wall',
                    lambda: self.__change_state_with_action(self.__remove_wall, self.__add_choice_widgets)
                )
            ))
        ]

    def __change_state_with_action(self, action_callback, next_state):
        action_callback()
        self.__remove_current_state_widgets()
        self.__current_state_widgets = next_state()

    def __change_state(self, new_state_callback):
        self.__remove_current_state_widgets()
        self.__current_state_widgets = new_state_callback()

    def __delete_state_widgets(self, widget_list):
        for widget in widget_list:
            self.maze_creation_menu.remove_widget(widget)

    def __add_cell_input(self, action_text, action_callback):
        return [
            self.maze_creation_menu.add.text_input(
                title='Row: ',
                maxchar=2,

            ),
            self.maze_creation_menu.add.text_input(
                title='Column: ',
                maxchar=2
            ),
            self.maze_creation_menu.add.button(action_text, action_callback),
            self.maze_creation_menu.add.button('Cancel', lambda: self.__change_state(
                lambda: self.__add_choice_widgets()
            ))
        ]

    def __add_wall(self):
        return None

    def __remove_wall(self):
        return None

    @property
    def __mode_choice_widgets(self):
        return [
            pygame_menu.widgets.Button('Add Wall'),
            pygame_menu.widgets.Button('Remove Wall')
        ]

    @property
    def maze_creation_menu(self):
        return self.__maze_creation_menu
