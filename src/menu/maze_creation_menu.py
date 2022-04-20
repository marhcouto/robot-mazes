import pygame
import pygame_menu
from src.model.game_model import GameModel, Maze, Position
from src.view.game_view import GameView


class MazeCreationMenu:
    def __init__(self, window_size, selected_algorithm):
        self.__window_size = window_size
        self.__maze_creation_menu = pygame_menu.Menu(
            height=self.__window_size[1],
            width=self.__window_size[0],
            title='Create your maze',
            theme=pygame_menu.themes.THEME_DARK,
            rows=7,
            columns=2
        )
        self.__selected_algorithm = selected_algorithm
        self.__reset_maze_surface()
        self.__internal_state = GameModel(Maze(0, None, None, []), 0)
        self.__current_state_widgets = self.__add_choice_widgets()

    def __remove_current_state_widgets(self):
        for widget in self.__current_state_widgets:
            self.maze_creation_menu.remove_widget(widget)
        self.__current_state_widgets = []

    def __update_maze_size(self, new_size):
        if new_size.isdigit():
            self.__internal_state = GameModel(Maze(int(new_size), None, None, []), 0)

    def __add_choice_widgets(self):
        maze_size = self.maze_creation_menu.add.text_input(
            'Size: ',
            maxchar=1,
            onreturn=self.__update_maze_size
        )
        if self.__internal_state.maze.size:
            maze_size.set_value(str(self.__internal_state.maze.size))
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
                lambda: self.__add_orig_dest_cell_input(
                    'Add Wall',
                    self.__add_wall
                )
            )),
            self.maze_creation_menu.add.button('Remove Wall', lambda: self.__change_state(
                lambda: self.__add_orig_dest_cell_input(
                    'Remove Wall',
                    self.__remove_wall
                )
            )),
            self.maze_creation_menu.add.none_widget(),
            self.maze_creation_menu.add.none_widget(),
            self.maze_creation_menu.add.surface(self.__maze_render_surface)
        ]

    @property
    def __internal_state_valid(self):
        return self.__internal_state.maze.init_robot_pos and self.__internal_state.maze.final_robot_pos and self.__internal_state.maze.size != 0

    def __reset_maze_surface(self):
        self.__maze_render_surface = pygame.Surface((550, 550))

    def __change_state(self, new_state_callback):
        self.__reset_maze_surface()
        self.__remove_current_state_widgets()
        self.__current_state_widgets = new_state_callback()
        if self.__internal_state_valid:
            game_view = GameView(self.__maze_render_surface, self.__internal_state)
            game_view.draw_static()
            game_view.draw_dynamic(self.__internal_state.maze.inital_robot_pos)

    def __delete_state_widgets(self, widget_list):
        for widget in widget_list:
            self.maze_creation_menu.remove_widget(widget)

    def __add_cell_input(self, action_text, action_callback):
        initial_row = self.maze_creation_menu.add.text_input(
            title='Row: ',
            maxchar=1,
        )
        initial_column = self.maze_creation_menu.add.text_input(
            title='Column: ',
            maxchar=1
        )
        return [
            initial_row,
            initial_column,
            self.maze_creation_menu.add.button(
                action_text,
                lambda: self.__commit_cell_input(
                    (initial_row.get_value(), initial_column.get_value()),
                    action_callback)
            ),
            self.maze_creation_menu.add.button('Cancel', lambda: self.__change_state(
                lambda: self.__add_choice_widgets()
            )),
            self.maze_creation_menu.add.none_widget(),
            self.maze_creation_menu.add.none_widget(),
            self.maze_creation_menu.add.none_widget(),
            self.maze_creation_menu.add.surface(self.__maze_render_surface)
        ]

    def __add_orig_dest_cell_input(self, action_text, action_callback):
        initial_row = self.maze_creation_menu.add.text_input(
            title='Initial Row: ',
            maxchar=1,
        )
        initial_column = self.maze_creation_menu.add.text_input(
            title='Initial Column: ',
            maxchar=1
        )
        final_row = self.maze_creation_menu.add.text_input(
            title='Final Row: ',
            maxchar=1,
        )
        final_column = self.maze_creation_menu.add.text_input(
            title='Final Column: ',
            maxchar=1
        )
        return [
            initial_row,
            initial_column,
            final_row,
            final_column,
            self.maze_creation_menu.add.button(
                action_text,
                lambda: self.__commit_cell_input(
                    ((initial_row.get_value(), initial_column.get_value()), (final_row.get_value(), final_column.get_value())),
                    action_callback
                )
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
            game_view = GameView(self.__maze_render_surface, self.__internal_state)
            game_view.draw_static()
            game_view.draw_dynamic(self.__internal_state.maze.init_robot_pos)

    def __set_init_pos(self, init_pos):
        if init_pos[0].isdigit() and init_pos[1].isdigit():
            self.__internal_state.maze.init_robot_pos = (int(init_pos[0]), int(init_pos[1]))

    def __set_final_pos(self, final_pos):
        if final_pos[0].isdigit() and final_pos[1].isdigit():
            self.__internal_state.maze.final_robot_pos = (int(final_pos[0]), int(final_pos[1]))

    def __add_wall(self, new_wall_pos):
        self.__internal_state.maze.add_wall(((Position(int(new_wall_pos[0][0]), int(new_wall_pos[0][1]))), (Position(int(new_wall_pos[1][0]), int(new_wall_pos[1][1])))))

    def __remove_wall(self, old_wall_pos):
        self.__internal_state.maze.remove_wall((Position(int(old_wall_pos[0][0]), int(old_wall_pos[0][1]))), (Position(int(old_wall_pos[1][0]), int(old_wall_pos[1][1]))))

    @property
    def __mode_choice_widgets(self):
        return [
            pygame_menu.widgets.Button('Add Wall'),
            pygame_menu.widgets.Button('Remove Wall')
        ]

    @property
    def maze_creation_menu(self):
        return self.__maze_creation_menu
