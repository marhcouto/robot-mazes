import pygame
import pygame_menu
from game import Maze
from game import maze_drawer

class MazeCreationMenu:
    def __init__(self, window_size, selected_algorithm):
        self.__window_size = window_size
        self.__maze_creation_menu = pygame_menu.Menu(
            height=self.__window_size[1],
            width=self.__window_size[0],
            title='Create your maze',
            theme=pygame_menu.themes.THEME_DARK,
            rows=5,
            columns=2
        )
        self.__selected_algorithm = selected_algorithm
        self.__reset_maze_surface()
        self.__internal_state = Maze(0, None, None, [])
        self.__current_state_widgets = self.__add_choice_widgets()

    def __remove_current_state_widgets(self):
        for widget in self.__current_state_widgets:
            self.maze_creation_menu.remove_widget(widget)
        self.__current_state_widgets = []

    def __update_maze_size(self, new_size):
        if new_size.isdigit():
            self.__internal_state = Maze(int(new_size), None, None, [])

    def __add_choice_widgets(self):
        maze_size = self.maze_creation_menu.add.text_input(
            'Size: ',
            maxchar=1,
            onreturn=self.__update_maze_size
        )
        if self.__internal_state.size:
            maze_size.set_value(str(self.__internal_state.size))
        return [
            maze_size,
            self.maze_creation_menu.add.button('Set Initial Position', lambda: self.__change_state(
                lambda: self.__add_cell_input(
                    'Set Initial Position',
                    self.__set_init_pos
                )
            )),
            self.maze_creation_menu.add.button('Set Final Position', lambda: self.__change_state(
                lambda: self.__add_cell_input(
                    'Set Final Position',
                    self.__set_final_pos
                )
            )),
            self.maze_creation_menu.add.button('Add Wall', lambda: self.__change_state(
                lambda: self.__add_cell_input(
                    'Add Wall',
                    self.__add_wall
                )
            )),
            self.maze_creation_menu.add.button('Remove Wall', lambda: self.__change_state(
                lambda: self.__add_cell_input(
                    'Remove Wall',
                    self.__remove_wall
                )
            )),
            self.maze_creation_menu.add.surface(self.__maze_render_surface)
        ]

    @property
    def __internal_state_valid(self):
        return self.__internal_state.init_robot_pos and self.__internal_state.final_robot_pos and self.__internal_state.size != 0

    def __reset_maze_surface(self):
        self.__maze_render_surface = pygame.Surface((550, 550))

    def __change_state(self, new_state_callback):
        self.__reset_maze_surface()
        self.__remove_current_state_widgets()
        self.__current_state_widgets = new_state_callback()
        if self.__internal_state_valid:
            maze_drawer(self.__internal_state, self.__maze_render_surface)

    def __delete_state_widgets(self, widget_list):
        for widget in widget_list:
            self.maze_creation_menu.remove_widget(widget)

    def __add_cell_input(self, action_text, action_callback):
        row = self.maze_creation_menu.add.text_input(
            title='Row: ',
            maxchar=2,
        )
        column = self.maze_creation_menu.add.text_input(
            title='Column: ',
            maxchar=2
        )
        return [
            row,
            column,
            self.maze_creation_menu.add.button(
                action_text,
                lambda: self.__commit_cell_input(
                    (row.get_value(), column.get_value()),
                    action_callback)
            ),
            self.maze_creation_menu.add.button('Cancel', lambda: self.__change_state(
                lambda: self.__add_choice_widgets()
            )),
            self.maze_creation_menu.add.none_widget(),
            self.maze_creation_menu.add.surface(self.__maze_render_surface)
        ]

    def __commit_cell_input(self, menu_data, action_callback):
        self.__reset_maze_surface()
        self.__remove_current_state_widgets()
        action_callback(menu_data)
        self.__current_state_widgets = self.__add_choice_widgets()
        if self.__internal_state_valid:
            maze_drawer(self.__internal_state, self.__maze_render_surface)

    def __set_init_pos(self, init_pos):
        if init_pos[0].isdigit() and init_pos[1].isdigit():
            self.__internal_state.init_robot_pos = (int(init_pos[0]), int(init_pos[1]))

    def __set_final_pos(self, final_pos):
        if final_pos[0].isdigit() and final_pos[1].isdigit():
            self.__internal_state.final_robot_pos = (int(final_pos[0]), int(final_pos[1]))

    def __add_wall(self, new_wall_pos):
        self.__internal_state.add_wall(new_wall_pos)

    def __remove_wall(self, old_wall_pos):
        self.__internal_state.remove_wall(old_wall_pos)

    @property
    def __mode_choice_widgets(self):
        return [
            pygame_menu.widgets.Button('Add Wall'),
            pygame_menu.widgets.Button('Remove Wall')
        ]

    @property
    def maze_creation_menu(self):
        return self.__maze_creation_menu
